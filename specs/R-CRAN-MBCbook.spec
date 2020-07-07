%global packname  MBCbook
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Companion Package for the Book "Model-Based Clustering andClassification for Data Science" by Bouveyron et al. (2019,ISBN:9781108644181).

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-Rmixmod 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-Rmixmod 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
The companion package provides all original data sets and functions that
are used in the book "Model-Based Clustering and Classification for Data
Science" by Charles Bouveyron, Gilles Celeux, T. Brendan Murphy and Adrian
E. Raftery (2019, ISBN:9781108644181).

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
%{rlibdir}/%{packname}/INDEX
