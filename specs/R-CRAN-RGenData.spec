%global packname  RGenData
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Generates Multivariate Nonnormal Data and Determines How ManyFactors to Retain

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The GenDataSample() and GenDataPopulation() functions create,
respectively, a sample or population of multivariate nonnormal data using
methods described in Ruscio and Kaczetow (2008). Both of these functions
call a FactorAnalysis() function to reproduce a correlation matrix. The
EFACompData() function allows users to determine how many factors to
retain in an exploratory factor analysis of an empirical data set using a
method described in Ruscio and Roche (2012). The latter function uses
populations of comparison data created by calling the GenDataPopulation()
function. <DOI: 10.1080/00273170802285693>. <DOI: 10.1037/a0025697>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
