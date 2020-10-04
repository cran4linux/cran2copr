%global packname  lconnect
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Simple Tools to Compute Landscape Connectivity Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-igraph 

%description
Provides functions to upload vectorial data and derive landscape
connectivity metrics in habitat or matrix systems. Additionally, includes
an approach to assess individual patch contribution to the overall
landscape connectivity, enabling the prioritization of habitat patches.
The computation of landscape connectivity and patch importance are very
useful in Landscape Ecology research. The metrics available are: number of
components, number of links, size of the largest component, mean size of
components, class coincidence probability, landscape coincidence
probability, characteristic path length, expected cluster size,
area-weighted flux and integral index of connectivity. Pascual-Hortal, L.,
and Saura, S. (2006) <doi:10.1007/s10980-006-0013-z> Urban, D., and Keitt,
T. (2001) <doi:10.2307/2679983> Laita, A., Kotiaho, J., Monkkonen, M.
(2011) <doi:10.1007/s10980-011-9620-4>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
