%global __brp_check_rpaths %{nil}
%global packname  SenSrivastava
%global packver   2015.6.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.6.25
Release:          3%{?dist}%{?buildtag}
Summary:          Datasets from Sen & Srivastava

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Collection of datasets from Sen & Srivastava: "Regression Analysis,
Theory, Methods and Applications", Springer.  Sources for individual data
files are more fully documented in the book.

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
