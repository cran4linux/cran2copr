%global __brp_check_rpaths %{nil}
%global packname  PatternClass
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Class-Focused Pattern Metric Comparisons using Simulation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-raster 

%description
NOTE: This content is being migrated to the package ShapePattern to
provide a comprehensive set of tools for shape and pattern analysis. All
future maintenance will be in that package -- please update your links.
This current package provides tools for estimating composition and
configuration parameters from a categorical (binary) landscape map (grid)
and then simulates a selected number of statistically similar landscapes.
Class-focused pattern metrics are computed for each simulated map to
produce empirical distributions against which statistical comparisons can
be made. The code permits the analysis of single maps or pairs of maps.
Current limitation is for binary (classes 1, 2) maps that are 64x64 cells
in extent.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
