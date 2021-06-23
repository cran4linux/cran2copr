%global __brp_check_rpaths %{nil}
%global packname  jointDiag
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Approximate Diagonalization of a Set of Square Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Different algorithms to perform approximate joint diagonalization of a
finite set of square matrices. Depending on the algorithm, orthogonal or
non-orthogonal diagonalizer is found. These algorithms are particularly
useful in the context of blind source separation. Original publications of
the algorithms can be found in Ziehe et al. (2004), Pham and Cardoso
(2001) <doi:10.1109/78.942614>, Souloumiac (2009)
<doi:10.1109/TSP.2009.2016997>, Vollgraff and Obermayer
<doi:10.1109/TSP.2006.877673>. An example of application in the context of
Brain-Computer Interfaces EEG denoising can be found in Gouy-Pailler et al
(2010) <doi:10.1109/TBME.2009.2032162>.

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
