import BlackPawn from "./images/black_pawn.svg"
import BlackKing from "./images/black_king.svg"
import BlackQueen from "./images/black_queen.svg"
import BlackKnight from "./images/black_knight.svg"
import BlackBishop from "./images/black_bishop.svg"
import BlackRook from "./images/black_rook.svg"
import WhitePawn from "./images/white_pawn.svg"
import WhiteKing from "./images/white_king.svg"
import WhiteQueen from "./images/white_queen.svg"
import WhiteKnight from "./images/white_knight.svg"
import WhiteBishop from "./images/white_bishop.svg"
import WhiteRook from "./images/white_rook.svg"

const getImg = (svg, alt) => {
  return <img src={svg} alt={alt} />
}

export const PIECES_SVG = {
  bp: getImg(BlackPawn, "Black Pawn"),
  bk: getImg(BlackKing, "Black King"),
  bq: getImg(BlackQueen, "Black Queen"),
  bn: getImg(BlackKnight, "Black Knight"),
  bb: getImg(BlackBishop, "Black Bishop"),
  br: getImg(BlackRook, "Black Rook"),
  wp: getImg(WhitePawn, "White Pawn"),
  wk: getImg(WhiteKing, "White King"),
  wq: getImg(WhiteQueen, "White Queen"),
  wn: getImg(WhiteKnight, "White Knight"),
  wb: getImg(WhiteBishop, "White Bishop"),
  wr: getImg(WhiteRook, "White Rook")
}
