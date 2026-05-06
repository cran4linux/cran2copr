%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reems
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Effective Migration Surfaces from Single Nucleotide Polymorphism Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-utils >= 3.3.2
BuildRequires:    R-CRAN-raster >= 2.4.15
BuildRequires:    R-CRAN-BH >= 1.76.0
BuildRequires:    R-CRAN-sp >= 1.1.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
Requires:         R-stats >= 3.3.2
Requires:         R-utils >= 3.3.2
Requires:         R-CRAN-raster >= 2.4.15
Requires:         R-CRAN-sp >= 1.1.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-sf 

%description
Wrapper and plotting utilities for the spatial population genetics tool
'EEMS' (Estimated Effective Migration Surfaces) for SNP (Single Nucleotide
Polymorphism) data, originally provided as a command-line tool written in
'C++' together with an accompanying 'R' package for plotting the output of
the 'EEMS' tool itself (<https://github.com/dipetkov/eems/>). There are
four main motivations for offering this to 'R' users as a package.
Firstly, to remove the installation and configuration burden for the
'EEMS' command-line tool, which relies on manually installed 'Boost' and
'Eigen' system libraries and configuring their location; secondly, to
streamline the workflow by having a singe environment (the 'R' system) for
the entire analysis rather than a file-based command-line executable whose
output files are then to be imported and analysed by a separate 'R'
script; thirdly, to make the input formats compatible with other,
'R'-based spatial population genetics tools such as the 'ConStruct'
package; and lastly, to allow for easily running several chains in
parallel and combining them for plotting and further analysis. The package
also adds more intuitive, streamlined tooling around creating more complex
habitats. The method of estimating effective migration surfaces was first
described by Petkova, D., Novembre, J. & Stephens, M. (2016)
<doi:10.1038/ng.3464>.

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
