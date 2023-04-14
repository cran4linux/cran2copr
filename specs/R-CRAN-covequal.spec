%global __brp_check_rpaths %{nil}
%global packname  covequal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Test for Equality of Covariance Matrices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RMTstat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-RMTstat 
Requires:         R-stats 
Requires:         R-CRAN-corpcor 

%description
Computes p-values using the largest root test using an approximation to
the null distribution by Johnstone (2008) <DOI:10.1214/08-AOS605>.

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
