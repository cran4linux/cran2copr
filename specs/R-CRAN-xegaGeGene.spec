%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaGeGene
%global packver   1.0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Grammatical Evolution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-xegaSelectGene 
BuildRequires:    R-CRAN-xegaBNF 
BuildRequires:    R-CRAN-xegaDerivationTrees 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-xegaSelectGene 
Requires:         R-CRAN-xegaBNF 
Requires:         R-CRAN-xegaDerivationTrees 

%description
Grammatical evolution (see O'Neil, M. and Ryan, C.
(2003,ISBN:1-4020-7444-1)) uses decoders to convert linear (binary or
integer genes) into programs. In addition, automatic determination of
codon precision with a limited rule choice bias is provided. For a recent
survey of grammatical evolution, see Ryan, C., O'Neill, M., and Collins,
J. J. (2018) <doi:10.1007/978-3-319-78717-6>.

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
