%global packname  STPGA
%global packver   5.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2.1
Release:          1%{?dist}
Summary:          Selection of Training Populations by Genetic Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-AlgDesign 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-emoa 
Requires:         R-grDevices 

%description
Combining Predictive Analytics and Experimental Design to Optimize
Results. To be utilized to select a test data calibrated training
population in high dimensional prediction problems and assumes that the
explanatory variables are observed for all of the individuals. Once a
"good" training set is identified, the response variable can be obtained
only for this set to build a model for predicting the response in the test
set. The algorithms in the package can be tweaked to solve some other
subset selection problems.

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
