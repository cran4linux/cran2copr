%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eiCircles
%global packver   0.0.1-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference of RxC Tables by Overdispersed-Multinomial Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-NlcOptim >= 0.6
BuildRequires:    R-stats 
Requires:         R-CRAN-NlcOptim >= 0.6
Requires:         R-stats 

%description
Estimates RxC (R by C) vote transfer matrices (ecological contingency
tables) from aggregate data using the model described in Forcina et al.
(2012), as extension of the model proposed in Brown and Payne (1986).
Allows incorporation of covariates. References: Brown, P. and Payne, C.
(1986). ''Aggregate data, ecological regression and voting transitions''.
Journal of the American Statistical Association, 81, 453–460.
<DOI:10.1080/01621459.1986.10478290>. Forcina, A., Gnaldi, M. and
Bracalente, B. (2012). ''A revised Brown and Payne model of voting
behaviour applied to the 2009 elections in Italy''. Statistical Methods &
Applications, 21, 109–119. <DOI:10.1007/s10260-011-0184-x>. Pavia, J.M,
and Forcina, A. (2026). ''Simulating electoral behavior''. Modeling
Decisions for Artificial Intelligence, MDAI 2025. Lecture Notes in
Computer Science, vol 15957, Torra, V., Narukawa, Y., Domingo-Ferrer, J.
(eds), Springer, Cham, pp. 54-65. <DOI:10.1007/978-3-032-00891-6_5>.
Acknowledgements: The authors wish to thank Consellería de Educación,
Cultura, Universidades y Empleo, Generalitat Valenciana (grant
CIAICO/2023/031) and MICIU/AEI/10.13039/501100011033/FEDER, EU (grant
PID2021-128228NB-I00) for supporting this research.

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
