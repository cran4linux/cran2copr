%global __brp_check_rpaths %{nil}
%global packname  ada
%global packver   2.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          The R Package Ada for Stochastic Boosting

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-rpart 
Requires:         R-rpart 

%description
Performs discrete, real, and gentle boost under both exponential and
logistic loss on a given data set.  The package ada provides a
straightforward, well-documented, and broad boosting routine for
classification, ideally suited for small to moderate-sized data sets.

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
