%global __brp_check_rpaths %{nil}
%global packname  edgebundleR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Circle Plot with Bundled Edges

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.3.2
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-htmlwidgets >= 0.3.2
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-shiny 

%description
Generates interactive circle plots with the nodes around the circumference
and linkages between the connected nodes using hierarchical edge bundling
via the D3 JavaScript library. See <http://d3js.org/> for more information
on D3.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
