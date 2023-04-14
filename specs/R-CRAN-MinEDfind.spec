%global __brp_check_rpaths %{nil}
%global packname  MinEDfind
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          A Bayesian Design for Minimum Effective Dosing-Finding Trial

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
The nonparametric two-stage Bayesian adaptive design is a novel phase II
clinical trial design for finding the minimum effective dose (MinED). This
design is motivated by the top priority and concern of clinicians when
testing a new drug, which is to effectively treat patients and minimize
the chance of exposing them to subtherapeutic or overly toxic doses. It is
used to design single-agent trials.

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
