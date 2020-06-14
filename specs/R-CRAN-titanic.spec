%global packname  titanic
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Titanic Passenger Survival Data Set

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch

%description
This data set provides information on the fate of passengers on the fatal
maiden voyage of the ocean liner "Titanic", summarized according to
economic status (class), sex, age and survival. Whereas the base R Titanic
data found by calling data("Titanic") is an array resulting from
cross-tabulating 2201 observations, these data sets are the individual
non-aggregated observations and formatted in a machine learning context
with a training sample, a testing sample, and two additional data sets
that can be used for deeper machine learning analysis. These data sets are
also the data sets downloaded from the Kaggle competition and thus lowers
the barrier to entry for users new to R or machine learing.

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
%{rlibdir}/%{packname}/data-raw
%{rlibdir}/%{packname}/INDEX
