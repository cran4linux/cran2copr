%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boodd
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for the Book "Bootstrap for Dependent Data, with an R Package"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-geoR 
Requires:         R-stats 
Requires:         R-CRAN-tseries 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-geoR 

%description
Companion package, functions, data sets, examples for the book Patrice
Bertail and Anna Dudek (2025), Bootstrap for Dependent Data, with an R
package (by Bernard Desgraupes and Karolina Marek) - submitted. Kreiss,
J.-P. and Paparoditis, E. (2003) <doi:10.1214/aos/1074290332> Politis,
D.N., and White, H. (2004) <doi:10.1081/ETC-120028836> Patton, A.,
Politis, D.N., and White, H. (2009) <doi:10.1080/07474930802459016>
Tsybakov, A. B. (2018) <doi:10.1007/b13794> Bickel, P., and Sakov, A.
(2008) <doi:10.1214/18-AOS1803> Götze, F. and Račkauskas, A. (2001)
<doi:10.1214/lnms/1215090074> Politis, D. N., Romano, J. P., & Wolf, M.
(1999, ISBN:978-0-387-98854-2) Carlstein E. (1986)
<doi:10.1214/aos/1176350057> Künsch, H. (1989)
<doi:10.1214/aos/1176347265> Liu, R. and Singh, K. (1992)
<https://www.stat.purdue.edu/docs/research/tech-reports/1991/tr91-07.pdf>
Politis, D.N. and Romano, J.P. (1994) <doi:10.1080/01621459.1994.10476870>
Politis, D.N. and Romano, J.P. (1992)
<https://www.stat.purdue.edu/docs/research/tech-reports/1991/tr91-07.pdf>
Patrice Bertail, Anna E. Dudek. (2022) <doi:10.3150/23-BEJ1683> Dudek,
A.E., Leśkow, J., Paparoditis, E. and Politis, D. (2014a)
<https://ideas.repec.org/a/bla/jtsera/v35y2014i2p89-114.html> Beran, R.
(1997) <doi:10.1023/A:1003114420352> B. Efron, and Tibshirani, R. (1993,
ISBN:9780429246593) Bickel, P. J., Götze, F. and van Zwet, W. R. (1997)
<doi:10.1007/978-1-4614-1314-1_17> A. C. Davison, D. Hinkley (1997)
<doi:10.2307/1271471> Falk, M., & Reiss, R. D. (1989)
<doi:10.1007/BF00354758> Lahiri, S. N. (2003)
<doi:10.1007/978-1-4757-3803-2> Shimizu, K. .(2017)
<doi:10.1007/978-3-8348-9778-7> Park, J.Y. (2003)
<doi:10.1111/1468-0262.00471> Kirch, C. and Politis, D. N. (2011)
<doi:10.48550/arXiv.1211.4732> Bertail, P. and Dudek, A.E. (2024)
<doi:10.3150/23-BEJ1683> Dudek, A. E. (2015)
<doi:10.1007/s00184-014-0505-9> Dudek, A. E. (2018)
<doi:10.1080/10485252.2017.1404060> Bertail, P., Clémençon, S. (2006a)
<https://ideas.repec.org/p/crs/wpaper/2004-47.html> Bertail, P. and
Clémençon, S. (2006, ISBN:978-0-387-36062-1) Radulović, D. (2006)
<doi:10.1007/BF02603005> Bertail, P. Politis, D. N. Rhomari, N. (2000)
<doi:10.1080/02331880008802701> Nordman, D.J. Lahiri, S.N.(2004)
<doi:10.1214/009053604000000779> Politis, D.N. Romano, J.P. (1993)
<doi:10.1006/jmva.1993.1085> Hurvich, C. M. and Zeger, S. L. (1987,
ISBN:978-1-4612-0099-4) Bertail, P. and Dudek, A. (2021)
<doi:10.1214/20-EJS1787> Bertail, P., Clémençon, S. and Tressou, J. (2015)
<doi:10.1111/jtsa.12105> Asmussen, S. (1987)
<doi:10.1007/978-3-662-11657-9> Efron, B. (1979)
<doi:10.1214/aos/1176344552> Gray, H., Schucany, W. and Watkins, T. (1972)
<doi:10.2307/2335521> Quenouille, M.H. (1949)
<doi:10.1111/j.2517-6161.1949.tb00023.x> Quenouille, M. H. (1956)
<doi:10.2307/2332914> Prakasa Rao, B. L. S. and Kulperger, R. J. (1989)
<https://www.jstor.org/stable/25050735> Rajarshi, M.B. (1990)
<doi:10.1007/BF00050835> Dudek, A.E. Maiz, S. and Elbadaoui, M. (2014)
<doi:10.1016/j.sigpro.2014.04.022> Beran R. (1986)
<doi:10.1214/aos/1176349847> Maritz, J. S. and Jarrett, R. G. (1978)
<doi:10.2307/2286545> Bertail, P., Politis, D., Romano, J. (1999)
<doi:10.2307/2670177> Bertail, P. and Clémençon, S. (2006b)
<doi:10.1007/0-387-36062-X_1> Radulović, D. (2004)
<doi:10.1007/BF02603005> Hurd, H.L., Miamee, A.G. (2007)
<doi:10.1002/9780470182833> Bühlmann, P. (1997) <doi:10.2307/3318584>
Choi, E., Hall, P. (2000) <doi:10.1111/1467-9868.00244> Efron, B.,
Tibshirani, R. (1993, ISBN:9780429246593) Bertail, P., Clémençon, S. and
Tressou, J. (2009) <doi:10.1007/s10687-009-0081-y> Bertail, P.,
Medina-Garay, A., De Lima-Medina, F. and Jales, I. (2024)
<doi:10.1080/02331888.2024.2344670>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
