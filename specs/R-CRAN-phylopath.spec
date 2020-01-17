%global packname  phylopath
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Perform Phylogenetic Path Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-phylolm >= 2.5
BuildRequires:    R-CRAN-ggm >= 2.3
BuildRequires:    R-CRAN-pbapply >= 1.3.2
BuildRequires:    R-CRAN-MuMIn >= 1.15.6
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-ggraph >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ape >= 4.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-phylolm >= 2.5
Requires:         R-CRAN-ggm >= 2.3
Requires:         R-CRAN-pbapply >= 1.3.2
Requires:         R-CRAN-MuMIn >= 1.15.6
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-ggraph >= 1.0.0
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-parallel 
Requires:         R-CRAN-tibble 

%description
A comprehensive and easy to use R implementation of confirmatory
phylogenetic path analysis as described by Von Hardenberg and
Gonzalez-Voyer (2012) <doi:10.1111/j.1558-5646.2012.01790.x>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
