%global packname  likelihoodAsy
%global packver   0.51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.51
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Likelihood Asymptotics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cond 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-cond 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-pracma 

%description
Functions for computing the r and r* statistics for inference on an
arbitrary scalar function of model parameters, plus some code for the
(modified) profile likelihood.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
