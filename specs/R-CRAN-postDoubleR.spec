%global packname  postDoubleR
%global packver   1.4.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.12
Release:          3%{?dist}%{?buildtag}
Summary:          Post Double Selection with Double Machine Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Implements post double selection using double machine learning, see
Chernozhukov, Chetverikov, Demirer, Duflo, Hansen, Newey, Robins (2017)
<doi:10.1111/ectj.12097>, for various models, using several back ends.
Allows the user flexibility in specifying their own methods for
estimation.

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
%{rlibdir}/%{packname}/INDEX
