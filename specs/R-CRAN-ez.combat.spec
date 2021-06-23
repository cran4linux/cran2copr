%global __brp_check_rpaths %{nil}
%global packname  ez.combat
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy ComBat Harmonization

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A dataframe-friendly implementation of ComBat Harmonization which uses an
empirical Bayesian framework to remove batch effects. Johnson WE & Li C
(2007) <doi:10.1093/biostatistics/kxj037> "Adjusting batch effects in
microarray expression data using empirical Bayes methods." Fortin J-P,
Cullen N, Sheline YI, Taylor WD, Aselcioglu I, Cook PA, Adams P, Cooper C,
Fava M, McGrath PJ, McInnes M, Phillips ML, Trivedi MH, Weissman MM, &
Shinohara RT (2017) <doi:10.1016/j.neuroimage.2017.11.024> "Harmonization
of cortical thickness measurements across scanners and sites." Fortin J-P,
Parker D, Tun<e7> B, Watanabe T, Elliott MA, Ruparel K, Roalf DR,
Satterthwaite TD, Gur RC, Gur RE, Schultz RT, Verma R, & Shinohara RT
(2017) <doi:10.1016/j.neuroimage.2017.08.047> "Harmonization of multi-site
diffusion tensor imaging data."

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
