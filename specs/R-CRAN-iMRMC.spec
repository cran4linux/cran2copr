%global __brp_check_rpaths %{nil}
%global packname  iMRMC
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Multi-Reader, Multi-Case Analysis Methods (ROC, Agreement, andOther Metrics)

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Do Multi-Reader, Multi-Case (MRMC) analyses of data from imaging studies
where clinicians (readers) evaluate patient images (cases). What does this
mean? ... Many imaging studies are designed so that every reader reads
every case in all modalities, a fully-crossed study. In this case, the
data is cross-correlated, and we consider the readers and cases to be
cross-correlated random effects. An MRMC analysis accounts for the
variability and correlations from the readers and cases when estimating
variances, confidence intervals, and p-values. The functions in this
package can treat arbitrary study designs and studies with missing data,
not just fully-crossed study designs. The initial package analyzes the
reader-average area under the receiver operating characteristic (ROC)
curve with U-statistics according to Gallas, Bandos, Samuelson, and Wagner
2009 <doi:10.1080/03610920802610084>. Additional functions analyze other
endpoints with U-statistics (binary performance and score differences)
following the work by Gallas, Pennello, and Myers 2007
<doi:10.1364/JOSAA.24.000B70>. Package development and documentation is at
<https://github.com/DIDSR/iMRMC/tree/master>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data-raw
%doc %{rlibdir}/%{packname}/extra
%{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
