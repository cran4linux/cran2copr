%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtpcrm
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dose Transition Pathways for Continual Reassessment Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-dfcrm 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-dfcrm 

%description
Provides the dose transition pathways (DTP) to project in advance the
doses recommended by a model-based design for subsequent patients (stay,
escalate, deescalate or stop early) using all the accumulated toxicity
information; See Yap et al (2017) <doi:10.1158/1078-0432.CCR-17-0582>. DTP
can be used as a design and an operational tool and can be displayed as a
table or flow diagram. The 'dtpcrm' package also provides the modified
continual reassessment method (CRM) and time-to-event CRM (TITE-CRM) with
added practical considerations to allow stopping early when there is
sufficient evidence that the lowest dose is too toxic and/or there is a
sufficient number of patients dosed at the maximum tolerated dose.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
