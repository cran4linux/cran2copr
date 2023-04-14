%global __brp_check_rpaths %{nil}
%global packname  c2c
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Compare Two Classifications or Clustering Solutions of VaryingStructure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
Compare two classifications or clustering solutions that may or may not
have the same number of classes, and that might have hard or soft (fuzzy,
probabilistic) membership. Calculate various metrics to assess how the
clusters compare to each other. The calculations are simple, but provide a
handy tool for users unfamiliar with matrix multiplication. This package
is not geared towards traditional accuracy assessment for classification/
mapping applications - the motivating use case is for comparing a
probabilistic clustering solution to a set of reference or existing class
labels that could have any number of classes (that is, without having to
degrade the probabilistic clustering to hard classes).

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
