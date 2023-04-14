%global __brp_check_rpaths %{nil}
%global packname  OOBCurve
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Out of Bag Learning Curve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr >= 2.11
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-mlr >= 2.11
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 

%description
Provides functions to calculate the out-of-bag learning curve for random
forests for any measure that is available in the 'mlr' package. Supported
random forest packages are 'randomForest' and 'ranger' and trained models
of these packages with the train function of 'mlr'. The main function is
OOBCurve() that calculates the out-of-bag curve depending on the number of
trees. With the OOBCurvePars() function out-of-bag curves can also be
calculated for 'mtry', 'sample.fraction' and 'min.node.size' for the
'ranger' package.

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
