%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evolved
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Open Software for Teaching Evolutionary Biology at Multiple Scales Through Virtual Inquiries

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-diversitree 
BuildRequires:    R-CRAN-phytools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-diversitree 
Requires:         R-CRAN-phytools 

%description
"Evolutionary Virtual Education" - 'evolved' - provides multiple tools to
help educators (especially at the graduate level or in advanced
undergraduate level courses) apply inquiry-based learning in general
evolution classes. In particular, the tools provided include functions
that simulate evolutionary processes (e.g., genetic drift, natural
selection within a single locus) or concepts (e.g. Hardy-Weinberg
equilibrium, phylogenetic distribution of traits). More than only
simulating, the package also provides tools for students to analyze (e.g.,
measuring, testing, visualizing) datasets with characteristics that are
common to many fields related to evolutionary biology. Importantly, the
package is heavily oriented towards providing tools for inquiry-based
learning - where students follow scientific practices to actively
construct knowledge. For additional details, see package's vignettes.

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
