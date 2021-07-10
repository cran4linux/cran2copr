%global __brp_check_rpaths %{nil}
%global packname  Rwave
%global packver   2.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Frequency Analysis of 1-D Signals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14

%description
A set of R functions which provide an environment for the Time-Frequency
analysis of 1-D signals (and especially for the wavelet and Gabor
transforms of noisy signals). It was originally written for Splus by Rene
Carmona, Bruno Torresani, and Wen L. Hwang, first at the University of
California at Irvine and then at Princeton University.  Credit should also
be given to Andrea Wang whose functions on the dyadic wavelet transform
are included. Rwave is based on the book: "Practical Time-Frequency
Analysis: Gabor and Wavelet Transforms with an Implementation in S", by
Rene Carmona, Wen L. Hwang and Bruno Torresani (1998, eBook
ISBN:978008053942), Academic Press.

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
