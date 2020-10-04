%global packname  UPMASK
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Unsupervised Photometric Membership Assignment in StellarClusters

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dimRed 
BuildRequires:    R-CRAN-loe 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dimRed 
Requires:         R-CRAN-loe 

%description
An implementation of the UPMASK method for performing membership
assignment in stellar clusters in R. It is prepared to use photometry and
spatial positions, but it can take into account other types of data. The
method is able to take into account arbitrary error models, and it is
unsupervised, data-driven, physical-model-free and relies on as few
assumptions as possible. The approach followed for membership assessment
is based on an iterative process, dimensionality reduction, a clustering
algorithm and a kernel density estimation.

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
