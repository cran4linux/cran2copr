%global packname  ScorePlus
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Implementation of SCORE, SCORE+ and Mixed-SCORE

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-igraphdata 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-igraphdata 
Requires:         R-stats 

%description
Implementation of community detection algorithm SCORE in the paper J. Jin
(2015) <arXiv:1211.5803>, and SCORE+ in J. Jin, Z. Ke and S. Luo (2018)
<arXiv:1811.05927>. Membership estimation algorithm called Mixed-SCORE in
J. Jin, Z. Ke and S. Luo (2017) <arXiv:1708.07852>.

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
%{rlibdir}/%{packname}/INDEX
