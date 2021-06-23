%global __brp_check_rpaths %{nil}
%global packname  stepp
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Subpopulation Treatment Effect Pattern Plot (STEPP)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
Requires:         R-methods 
Requires:         R-CRAN-car 
Requires:         R-CRAN-survival 
Requires:         R-splines 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 

%description
A method to explore the treatment-covariate interactions in survival or
generalized linear model (GLM) for continuous, binomial and count data
arising from two or more treatment arms of a clinical trial. A permutation
distribution approach to inference is implemented, based on permuting the
covariate values within each treatment group. Bonetti M, Gelber RD (2004)
<DOI:10.1093/biostatistics/5.3.465>. Marco Bonetti, David Zahrieh, Bernard
F. Cole, and Richard D. Gelber (2009) <doi:10.1002/sim.3524>. Ann A.
Lazar, Bernard F. Cole, Marco Bonetti, and Richard D. Gelber (2010)
<doi:10.1200/JCO.2009.27.9182>. Lazar AA,Bonetti M,Cole BF,Yip WK,Gelber
RD (2016) <doi:10.1177/1740774515609106>. Wai-Ki Yip,Marco Bonetti,Bernard
F Cole,William Barcella,Xin Victoria Wang,Ann Lazar,and Richard D Gelber
(2016) <doi:10.1177/1740774516643297>. Wang XV, Cole B, Bonetti M, Gelber
RD (2016) <doi:10.1002/sim.6958>. Wai-Ki Yip (2017,
ISBN:978-3-319-48846-2).

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
