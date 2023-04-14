%global __brp_check_rpaths %{nil}
%global packname  agRee
%global packver   0.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          3%{?dist}%{?buildtag}
Summary:          Various Methods for Measuring Agreement

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0.4
BuildRequires:    R-CRAN-coda >= 0.16.1
BuildRequires:    R-CRAN-miscF >= 0.1.4
BuildRequires:    R-CRAN-R2jags >= 0.03.11
Requires:         R-CRAN-lme4 >= 1.0.4
Requires:         R-CRAN-coda >= 0.16.1
Requires:         R-CRAN-miscF >= 0.1.4
Requires:         R-CRAN-R2jags >= 0.03.11

%description
Bland-Altman plot and scatter plot with identity line for visualization
and point and interval estimates for different metrics related to
reproducibility/repeatability/agreement including the concordance
correlation coefficient, intraclass correlation coefficient,
within-subject coefficient of variation, smallest detectable difference,
and mean normalized smallest detectable difference.

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
%{rlibdir}/%{packname}
