%global __brp_check_rpaths %{nil}
%global packname  bcc
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Beta Control Charts

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-methods 
Requires:         R-CRAN-qcc 
Requires:         R-methods 

%description
Applies beta control charts to defined values, using 'qcc' package with
new beta control limits. The Beta Chart presents the control limits based
on the Beta probability distribution. Can be used for monitoring fraction
data from Binomial distribution as replacement of the p-Charts. The Beta
Chart was applied for monitoring the variables in three real studies, and
it was compared to the control limits with three schemes. The comparative
analysis showed that: (i) Beta approximation to the Binomial distribution
was more appropriate with values confined in the [0, 1]- interval; and
(ii) the charts proposed were more sensitive to the average run length
(ARL), in both in-control and out-of-control processes monitoring. The
Beta Charts outperform the Shewhart control charts analyzed for monitoring
fraction data. Ângelo Márcio Oliveira Sant’Anna, Carla Schwengber ten
Caten (2012) <doi:10.1016/j.eswa.2012.02.146>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
