%global __brp_check_rpaths %{nil}
%global packname  smbinning
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Scoring Modeling and Optimal Binning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gsubfn 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gsubfn 

%description
A set of functions to build a scoring model from beginning to end, leading
the user to follow an efficient and organized development process,
reducing significantly the time spent on data exploration, variable
selection, feature engineering, binning and model selection among other
recurrent tasks. The package also incorporates monotonic and customized
binning, scaling capabilities that transforms logistic coefficients into
points for a better business understanding and calculates and visualizes
classic performance metrics of a classification model.

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
