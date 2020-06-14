%global packname  micromapST
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Linked Micromap Plots for General U. S. and Other GeographicAreas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-labeling 
Requires:         R-utils 

%description
Provides the users with the ability to quickly create Linked Micromap
plots for a collection of geographic areas. Linked Micromaps are
visualizations of georeferenced data that link statistical graphics to an
organized series of small maps or graphic images. The Help description
contains examples of how to use the micromapST function. Contained in this
package are border group datasets to support creating micromaps for the 50
U.S. states and District of Columbia (51 areas), the U. S. 20 Seer
Registries, the 105 counties in the state of Kansas, the 62 counties of
New York, the 24 counties of Maryland, the 29 counties of Utah, the 32
administrative areas in China, the 218 administrative areas in the UK and
Ireland (for testing only), the 25 districts in the city of Seoul South
Korea, and the 52 counties on the Africa continent. A border group dataset
contains the boundaries related to the data level areas, a second layer
boundaries, a top or third layer boundary, a parameter list of run
options, and a cross indexing table between area names, abbreviations,
numeric identification and alias matching strings for the specific
geographic area.  By specifying a border group, the package create
micromaps for any geographic region.  The user can create and provide
their own border group dataset for any area beyond the areas contained
within the package. Copyrighted 2013, 2014, 2015 and 2016 by Carr, Pearson
and Pickle.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
