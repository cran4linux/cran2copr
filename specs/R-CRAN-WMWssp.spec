%global __brp_check_rpaths %{nil}
%global packname  WMWssp
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Wilcoxon-Mann-Whitney Sample Size Planning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
Calculates the minimal sample size for the Wilcoxon-Mann-Whitney test that
is needed for a given power and two sided type I error rate. The method
works for metric data with and without ties, count data, ordered
categorical data, and even dichotomous data. But data is needed for the
reference group to generate synthetic data for the treatment group based
on a relevant effect. For details, see Brunner, E., Bathke A. C. and
Konietschke, F: Rank- and Pseudo-Rank Procedures in Factorial Designs -
Using R and SAS, Springer Verlag, to appear.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
