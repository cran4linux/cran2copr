%global packname  cpk
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Clinical Pharmacokinetics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch

%description
The package cpk provides simplified clinical pharmacokinetic functions for
dose regimen design and modification at the point-of-care. Currently, the
following functions are available: (1) ttc.fn for target therapeutic
concentration, (2) dr.fn for dose rate, (3) di.fn for dosing interval, (4)
dm.fn for maintenance dose, (5) bc.ttc.fn for back calculation, (6) ar.fn
for accumulation ratio, (7) dpo.fn for orally administered dose, (8)
cmax.fn for peak concentration, (9) css.fn for steady-state concentration,
(10) cmin.fn for trough,(11) ct.fn for concentration-time predictions,
(12) dlcmax.fn for calculating loading dose based on drug's maximum
concentration, (13) dlar.fn for calculating loading dose based on drug's
accumulation ratio, and (14) R0.fn for calculating drug infusion rate.
Reference: Linares O, Linares A. Computational opioid prescribing: A novel
application of clinical pharmacokinetics. J Pain Palliat Care Pharmacother
2011;25:125-135.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
