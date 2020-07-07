%global packname  sisal
%global packver   0.48
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.48
Release:          3%{?dist}
Summary:          Sequential Input Selection Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-boot 
BuildRequires:    R-lattice 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-R.methodsS3 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-boot 
Requires:         R-lattice 
Requires:         R-mgcv 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-R.methodsS3 

%description
Implements the SISAL algorithm by Tikka and Hollmén. It is a sequential
backward selection algorithm which uses a linear model in a
cross-validation setting. Starting from the full model, one variable at a
time is removed based on the regression coefficients. From this set of
models, a parsimonious (sparse) model is found by choosing the model with
the smallest number of variables among those models where the validation
error is smaller than a threshold. Also implements extensions which
explore larger parts of the search space and/or use ridge regression
instead of ordinary least squares.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/toyDataSrc
%{rlibdir}/%{packname}/INDEX
