%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROCModels
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          ROC Models and AUC Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kedd 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-ROCit 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-doRNG 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kedd 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-ROCit 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-nor1mix 
Requires:         R-parallel 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-doRNG 

%description
The receiver operating characteristic (ROC) curve is one of the most
widely used tools for evaluating diagnostic and prognostic biomarkers
across diverse scientific fields, particularly in medicine. Despite its
ubiquity, ROC estimation and testing methods differ substantially in their
assumptions and resulting curve properties. This package provides a
unified framework for constructing, visualizing, and comparing parametric,
nonparametric, semiparametric, and Bayesian ROC curves. 'ROCModels' helps
researchers identify and implement ROC inference methods most suitable for
their data. See the accompanying vignette 'ROCModels_Package_Doc' for a
detailed introduction. Alonzo, T. A., and Pepe, M. S. (2002) <doi:
10.1093/biostatistics/3.3.421>, Andrews, D. F., and Herzberg, A. M. (1985)
<doi: 10.1007/978-1-4612-5098-2>, Bamber, D. (1975) <doi:
10.1016/0022-2496(75)90001-2>, Cox, D. R. (1972)
<doi:10.1111/j.2517-6161.1972.tb00899.x>, Cox, D. R. (1975) <doi:
10.1093/biomet/62.2.269>, DeLong, E. R., DeLong, D. M., and
Clarke-Pearson, D. L. (1988) <doi: 10.2307/2531595>, Dorfman, D. D., and
Alf, E. (1969) <doi: 10.1016/0022-2496(69)90019-4>, Dorfman, D. D.,
Berbaum, K. S., and Metz, C. E. (1997) <doi:
10.1016/s1076-6332(97)80013-x>, Erkanli, A., Sung, L., and Stamey, J. D.
(2006) <doi: 10.1002/sim.2496>, Faraggi, D., and Reiser, B. (2002) <doi:
10.1002/sim.1228>, Ghebremichael, M., and Habtemicael, S. (2018) <doi:
10.1080/02664763.2017.1420758>, Ghebremichael, M., and Michael, H. (2024)
<doi: 10.1080/03610918.2022.2032159>, Ghebremichael, M., Michael, H.,
Tubbs, J., and Paintsil, E. (2019) <doi: 10.3844/jmssp.2019.55.64>, Gönen,
M., and Heller, G. (2010) <doi: 10.1177/0272989X09360067>, Gopalakrishnan,
V., Bose, E., Nair, U., Cheng, Y., and Ghebremichael, M. (2020) <doi:
10.1186/s12879-020-05458-w>, Green, D. M., and Swets, J. A. (1966,
ISBN:0471324205), Gu, J., and Ghosal, S. (2009) <doi:
10.1016/j.jspi.2008.09.014>, Gu, Y., Ghosal, S., and Roy, A. (2008) <doi:
10.1002/sim.3366>, Guidoum, A. C. (2020) <doi:
10.32614/CRAN.package.kedd>, <doi: 10.48550/arXiv.2012.06102>, Guo, B.
(2015)
<https://d-scholarship.pitt.edu/23590/1/Guo_Ben_thesis_12-2014.pdf>,
Hanley, J. A., and McNeil, B. J. (1982) <doi:
10.1148/radiology.143.1.7063747>, Hsieh, F., and Turnbull, B. W. (1996)
<doi: 10.1214/aos/1033066197>, Hussain, E. (2012) <doi:
10.6000/1927-5129.2012.08.02.09>, Ishwaran, H., and James, L. F. (2002)
<doi: 10.1198/106186002411>, Jokiel-Rokita, A., and Topolnicki, R. (2020)
<doi: 10.1016/j.csda.2019.106820>, Krzanowski, W. J., and Hand, D. J.
(2009) <doi: 10.1201/9781439800225>, Kundu, D., and Gupta, R. D. (2006)
<doi: 10.1109/TR.2006.874918>, Lloyd, C. J. (1998) <doi:
10.1080/01621459.1998.10473797>, Lehmann, E. L. (1953) <doi:
10.1214/aoms/1177729080>, Metz, C. E., Herman, B. A., and Shen, J. H.
(1998)
<doi:10.1002/(SICI)1097-0258(19980515)17:9%%3C1033::AID-SIM784%%3E3.0.CO;2-Z>,
Pepe, M. S. (2003) <doi: 10.1093/oso/9780198509844.001.0001>, Pundir, S.,
and Amala, R. (2014) <doi: 10.22237/jmasm/1398917940>, Silverman, B. W.
(2018) <doi: 10.1201/9781315140919>, Yeo, I. K., and Johnson, R. A. (2000)
<doi: 10.1093/biomet/87.4.954>, Zhou, X. H., McClish, D. K., and
Obuchowski, N. A. (2009) <doi: 10.1002/9780470906514>, Zou, K. H., Hall,
W. J., and Shapiro, D. E. (1997) <doi:
10.1002/(SICI)1097-0258(19971015)16:19%%3C2143::AID-SIM655%%3E3.0.CO;2-3>.

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
