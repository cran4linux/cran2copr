%global packname  ShapePattern
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Tools for Analyzing Shapes and Patterns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-raster 

%description
This is (1) An evolving and growing collection of tools for the
quantification, assessment, and comparison of shape and pattern. The
spatial decomposition of planar shapes using 'ShrinkShape' to
incrementally shrink shapes to extinction while computing area, perimeter,
and number of parts at each iteration of shrinking. The spectra of results
are returned in graphic and tabular formats. Additional utility tools for
handling data are provided and this package will be added to as more tools
are created, cleaned-up, and documented. (2) Provision of tools for
estimating composition and configuration parameters from a categorical
(binary) landscape map (grid) and then simulates a selected number of
statistically similar landscapes. Class-focused pattern metrics are
computed for each simulated map to produce empirical distributions against
which statistical comparisons can be made. The code permits the analysis
of single maps or pairs of maps. Current limitation is for binary (classes
1, 2) maps that are 64x64 cells in extent. (3) Counting the number of each
first-order pattern element and converting that information into both
frequency and probability vectors. See Remmel (2018)
<doi:10.3390/su10103413> and Remmel and Fortin (2013)
<doi:10.1007/s10980-013-9905-x>. NOTE: This is a consolidation of existing
packages ('PatternClass', 'ShapePattern') to begin warehousing all shape
and pattern code in a common package. Note that all future developments
will appear in this package and that 'PatternClass' will eventually be
archived.

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
