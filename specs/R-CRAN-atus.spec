%global packname  atus
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}
Summary:          American Time Use Survey Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Abridged data from the American Time Use Survey (ATUS) for years
2003-2016. The ATUS is an annual survey conducted on a sample of
individuals across the United States studying how individuals spent their
time over the course of a day. Individual respondents were interviewed
about what activities they did, during what times (rounded to 15 minute
increments), at what locations, and in the presence of which individuals.
The activities are subsequently encoded based on 3 separate tier codes for
classification. This package includes data from the multi-year ATUS
Activities, ATUS-CPS, and ATUS Respondents files were included. Columns
were selected based on completeness of data as well as presence on the
Frequently Used Variables list provided by the ATUS website. All activity
codes (other than code '50' for 'Unable to Code') were included.
Permission was obtained from the Bureau of Labor Statistics for inclusion
in this package. The full data can be obtained from
<http://www.bls.gov/tus/>.

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
