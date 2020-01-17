%global packname  econullnetr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Null Model Analysis for Ecological Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-gtools 

%description
Tools for using null models to analyse ecological networks (e.g. food
webs, flower-visitation networks, seed-dispersal networks) and detect
resource preferences or non-random interactions among network nodes. Tools
are provided to run null models, test for and plot preferences, plot and
analyse bipartite networks, and export null model results in a form
compatible with other network analysis packages. The underlying null model
was developed by Agusti et al. (2003) Molecular Ecology
<doi:10.1046/j.1365-294X.2003.02014.x> and the full application to
ecological networks by Vaughan et al. (2018) econullnetr: an R package
using null models to analyse the structure of ecological networks and
identify resource selection. Methods in Ecology & Evolution,
<doi.org/10.1111/2041-210X.12907>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
