%global __brp_check_rpaths %{nil}
%global packname  influence.ME
%global packver   0.9-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Detecting Influential Data in Mixed Effects Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-Matrix >= 1.0
BuildRequires:    R-lattice 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-Matrix >= 1.0
Requires:         R-lattice 

%description
Provides a collection of tools for detecting influential cases in
generalized mixed effects models. It analyses models that were estimated
using 'lme4'. The basic rationale behind identifying influential data is
that when single units are omitted from the data, models based on these
data should not produce substantially different estimates. To standardize
the assessment of how influential a (single group of) observation(s) is,
several measures of influence are common practice, such as Cook's
Distance. In addition, we provide a measure of percentage change of the
fixed point estimates and a simple procedure to detect changing levels of
significance.

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
