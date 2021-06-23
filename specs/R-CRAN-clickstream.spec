%global __brp_check_rpaths %{nil}
%global packname  clickstream
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analyzes Clickstreams Based on Markov Chains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-linprog 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ClickClust 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-linprog 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ClickClust 
Requires:         R-parallel 
Requires:         R-CRAN-data.table 

%description
A set of tools to read, analyze and write lists of click sequences on
websites (i.e., clickstream). A click can be represented by a number,
character or string. Clickstreams can be modeled as zero- (only computes
occurrence probabilities), first- or higher-order Markov chains.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
