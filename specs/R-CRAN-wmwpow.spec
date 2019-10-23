%global packname  wmwpow
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Precise and Accurate Power of the Wilcoxon-Mann-Whitney Rank-SumTest for a Continuous Variable

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-smoothmest 
BuildRequires:    R-MASS 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-smoothmest 
Requires:         R-MASS 

%description
Power calculator for the two-sample Wilcoxon-Mann-Whitney rank-sum test
for a continuous outcome (Mollan, Trumble, Reifeis et. al., Jan. 2019)
<arXiv:1901.04597>, (Mann and Whitney 1947) <doi:10.1214/aoms/1177730491>,
(Shieh, Jan, and Randles 2006) <doi:10.1080/10485250500473099>.

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
