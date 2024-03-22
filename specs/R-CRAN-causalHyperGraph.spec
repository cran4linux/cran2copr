%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalHyperGraph
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Drawing Causal Hypergraphs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-useful 
BuildRequires:    R-CRAN-cna 
BuildRequires:    R-utils 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-useful 
Requires:         R-CRAN-cna 
Requires:         R-utils 

%description
Draws causal hypergraph plots from models output by configurational
comparative methods such as Coincidence Analysis (CNA) or Qualitative
Comparative Analysis (QCA).

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
