%global packname  LMest
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          1%{?dist}
Summary:          Generalized Latent Markov Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-CRAN-Formula >= 1.2.3
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MultiLCIRT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mmm 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Formula >= 1.2.3
Requires:         R-MASS 
Requires:         R-CRAN-MultiLCIRT 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mmm 
Requires:         R-CRAN-mix 
Requires:         R-utils 
Requires:         R-graphics 

%description
Latent Markov models for longitudinal continuous and categorical data. See
Bartolucci, Pandolfi, Pennoni (2017)<doi:10.18637/jss.v081.i04>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
