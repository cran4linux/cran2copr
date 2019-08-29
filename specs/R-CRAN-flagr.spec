%global packname  flagr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Implementation of Flag Aggregation

License:          EUPL-1.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Three methods are implemented in R to facilitate the aggregations of flags
in official statistics. From the underlying flags the highest in the
hierarchy, the most frequent, or with the highest total weight is
propagated to the flag(s) for EU or other aggregates. Below there are some
reference documents for the topic:
<https://sdmx.org/wp-content/uploads/CL_OBS_STATUS_v2_1.docx>,
<https://sdmx.org/wp-content/uploads/CL_CONF_STATUS_1_2_2018.docx>,
<http://ec.europa.eu/eurostat/data/database/information>,
<http://www.oecd.org/sdd/33869551.pdf>,
<https://sdmx.org/wp-content/uploads/CL_OBS_STATUS_implementation_20-10-2014.pdf>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
