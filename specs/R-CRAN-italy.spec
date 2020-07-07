%global packname  italy
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          The Italian Survey on Household and Wealth, 2008 and 2010

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch

%description
Provides two record linkage data sets on the Italian Survey on Household
and Wealth, 2008 and 2010, a sample survey conducted by the Bank of Italy
every two years. The 2010 survey covered 13,702 individuals, while the
2008 survey covered 13,734 individuals. The following categorical
variables are included in this data set: year of birth, working status,
employment status, branch of activity, town size, geographical area of
birth, sex, whether or not Italian national, and highest educational level
obtained. Unique identifiers are available to assess the accuracy of one’s
method. Please see Steorts (2015) <DOI:10.1214/15-BA965SI> to find more
details about the data set.

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
