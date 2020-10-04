%global packname  lactcurves
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Lactation Curve Parameter Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-splines 
Requires:         R-CRAN-orthopolynom 
Requires:         R-splines 

%description
AllCurves() runs multiple lactation curve models and extracts selection
criteria for each model. This package summarises the most common lactation
curve models from the last century and provides a tool for researchers to
quickly decide on which model fits their data best to proceed with their
analysis. Start parameters were optimized based on a dataset with 1.7
million Holstein-Friesian cows. If convergence fails, the start parameters
need to be manually adjusted. The models included in the package are taken
from: (1) Michaelis-Menten: Michaelis, L. and M.L. Menten (1913).
<www.plantphys.info/plant_physiology/copyright/MichaelisMentenTranslation2.pdf>
(1a) Michaelis-Menten (Rook): Rook, A.J., J. France, and M.S. Dhanoa
(1993). <doi:10.1017/S002185960007684X> (1b) Michaelis-Menten +
exponential (Rook): Rook, A.J., J. France, and M.S. Dhanoa (1993).
<doi:10.1017/S002185960007684X> (2) Brody (1923): Brody, S., A.C.
Ragsdale, and C.W. Turner (1923). <doi:10.1085/jgp.5.6.777> (3) Brody
(1924): Brody, S., C.W. Tuner, and A.C. Ragsdale (1924).
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2140670/> (4) Schumacher:
Schumacher, F.X. (1939) in Thornley, J.H.M. and J. France (2007).
<https://books.google.com.au/books/about/Mathematical_Models_in_Agriculture.html?id=rlwBCRSHobcC&redir_esc=y>
(4a) Schumacher (Lopez et al. 2015): Lopez, S. J. France, N.E. Odongo,
R.A. McBride, E. Kebreab, O. AlZahal, B.W. McBride, and J. Dijkstra
(2015). <doi:10.3168/jds.2014-8132> (5) Parabolic exponential (Adediran):
Adediran, S.A., D.A. Ratkowsky, D.J. Donaghy, and A.E.O. Malau-Aduli
(2012). <doi:10.3168/jds.2011-4663> (6) Wood: Wood, P.D.P. (1967).
<doi:10.1038/216164a0> (6a) Wood reparameterized (Dhanoa): Dhanoa, M.S.
(1981). <doi:10.1017/S0003356100027276> (6b) Wood non-linear
(Cappio-Borlino): Cappio-Borlino, A., G. Pulina, and G. Rossi (1995).
<doi:10.1016/0921-4488(95)00713-U> (7) Quadratic Polynomial (Dave): Dave,
B.K. (1971) in Adediran, S.A., D.A. Ratkowsky, D.J. Donaghy, and A.E.O.
Malau-Aduli (2012). <doi:10.3168/jds.2011-4663> (8) Cobby and Le Du
(Vargas): Vargas, B., W.J. Koops, M. Herrero, and J.A.M Van Arendonk
(2000). <doi:10.3168/jds.S0022-0302(00)75005-3> (9) Papajcsik and Bodero
1: Papajcsik, I.A. and J. Bodero (1988). <doi:10.1017/S0003356100003275>
(10) Papajcsik and Bodero 2: Papajcsik, I.A. and J. Bodero (1988).
<doi:10.1017/S0003356100003275> (11) Papajcsik and Bodero 3: Papajcsik,
I.A. and J. Bodero (1988). <doi:10.1017/S0003356100003275> (12) Papajcsik
and Bodero 4: Papajcsik, I.A. and J. Bodero (1988).
<doi:10.1017/S0003356100003275> (13) Papajcsik and Bodero 6: Papajcsik,
I.A. and J. Bodero (1988). <doi:10.1017/S0003356100003275> (14) Mixed log
model 1 (Guo and Swalve): Guo, Z. and H.H. Swalve (1995).
<https://journal.interbull.org/index.php/ib/issue/view/11> (15) Mixed log
model 3 (Guo and Swalve): Guo, Z. and H.H. Swalve (1995).
<https://journal.interbull.org/index.php/ib/issue/view/11> (16)
Log-quadratic (Adediran et al. 2012): Adediran, S.A., D.A. Ratkowsky, D.J.
Donaghy, and A.E.O. Malau-Aduli (2012). <doi:10.3168/jds.2011-4663> (17)
Wilmink: J.B.M. Wilmink (1987). <doi:10.1016/0301-6226(87)90003-0> (17a)
modified Wilmink (Jakobsen): Jakobsen J.H., P. Madsen, J. Jensen, J.
Pedersen, L.G. Christensen, and D.A. Sorensen (2002).
<doi:10.3168/jds.S0022-0302(02)74231-8> (17b) modified Wilmink (Laurenson
& Strucken): in preparation (2019). (18) Bicompartemental (Ferguson and
Boston 1993): Ferguson, J.D., and R. Boston (1993) in Adediran, S.A., D.A.
Ratkowsky, D.J. Donaghy, and A.E.O. Malau-Aduli (2012).
<doi:10.3168/jds.2011-4663> (19) Dijkstra: Dijkstra, J., J. France, M.S.
Dhanoa, J.A. Maas, M.D. Hanigan, A.J. Rook, and D.E. Beever (1997).
<doi10.3168/jds.S0022-0302(97)76185-X> (20) Morant and Gnanasakthy
(Pollott et al 2000): Pollott, G.E. and E. Gootwine (2000).
<doi10.1017/S1357729800055028> (21) Morant and Gnanasakthy (Vargas et al
2000): Vargas, B., W.J. Koops, M. Herrero, and J.A.M Van Arendonk (2000).
<doi:10.3168/jds.S0022-0302(00)75005-3> (22) Morant and Gnanasakthy
(Adediran et al. 2012): Adediran, S.A., D.A. Ratkowsky, D.J. Donaghy, and
A.E.O. Malau-Aduli (2012). <doi:10.3168/jds.2011-4663> (23) Khandekar (Guo
and Swalve): Guo, Z. and H.H. Swalve (1995).
<https://journal.interbull.org/index.php/ib/issue/view/11> (24) Ali and
Schaeffer: Ali, T.E. and L.R. Schaeffer (1987).
<https://www.nrcresearchpress.com/doi/pdf/10.4141/cjas87-067> (25)
Fractional Polynomial (Elvira et al. 2013): Elvira, L., F. Hernandez, P.
Cuesta, S. Cano, J.-V. Gonzalez-Martin, and S. Astiz (2012).
<doi:10.1017/S175173111200239X> (26) Pollott multiplicative (Elvira):
Elvira, L., F. Hernandez, P. Cuesta, S. Cano, J.-V. Gonzalez-Martin, and
S. Astiz (2012). <doi:10.1017/S175173111200239X> (27) Pollott modified:
Adediran, S.A., D.A. Ratkowsky, D.J. Donaghy, and A.E.O. Malau-Aduli
(2012). <doi:10.3168/jds.2011-4663> (28) Monophasic Grossman: Grossman, M.
and W.J. Koops (1988). <doi:10.3168/jds.S0022-0302(88)79723-4> (29)
Monophasic Power Transformed (Grossman 1999): Grossman, M., S.M. Hartz,
and W.J. Koops (1999). <doi:10.3168/jds.S0022-0302(99)75464-0> (30)
Diphasic (Grossman 1999): Grossman, M., S.M. Hartz, and W.J. Koops (1999).
<doi:10.3168/jds.S0022-0302(99)75464-0> (31) Diphasic Power Transformed
(Grossman 1999): Grossman, M., S.M. Hartz, and W.J. Koops (1999).
<doi:10.3168/jds.S0022-0302(99)75464-0> (32) Legendre Polynomial (3th
order): Jakobsen J.H., P. Madsen, J. Jensen, J. Pedersen, L.G.
Christensen, and D.A. Sorensen (2002).
<doi:10.3168/jds.S0022-0302(02)74231-8> (33) Legendre Polynomial (4th
order): Jakobsen J.H., P. Madsen, J. Jensen, J. Pedersen, L.G.
Christensen, and D.A. Sorensen (2002).
<doi:10.3168/jds.S0022-0302(02)74231-8> (34) Legendre + Wilmink (Lidauer):
Lidauer, M. and E.A. Mantysaari (1999).
<https://journal.interbull.org/index.php/ib/article/view/417> (35) Natural
Cubic Spline (3 percentiles): White, I.M.S., R. Thompson, and S.
Brotherstone (1999). <doi:10.3168/jds.S0022-0302(99)75277-X> (36) Natural
Cubic Spline (4 percentiles): White, I.M.S., R. Thompson, and S.
Brotherstone (1999). <doi:10.3168/jds.S0022-0302(99)75277-X> (37) Natural
Cubic Spline (5 percentiles): White, I.M.S., R. Thompson, and S.
Brotherstone (1999) <doi:10.3168/jds.S0022-0302(99)75277-X> (38) Natural
Cubic Spline (defined knots according to Harrell 2001): Jr. Harrell, F.E.
(2001). <https://link.springer.com/book/10.1007/978-3-319-19425-7> The
selection criteria measure the goodness of fit of the model and include:
Residual standard error (RSE), R-square (R2), log likelihood, Akaike
information criterion (AIC), Akaike information criterion corrected
(AICC), Bayesian Information Criterion (BIC), Durbin Watson coefficient
(DW). The following model parameters are included: Residual sum of squares
(RSS), Residual standard deviation (RSD), F-value (F) based on F-ratio
test.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
