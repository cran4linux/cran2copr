%global packname  dtpcrm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
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
information; See Yap et al (2017) <doi: 10.1158/1078-0432.CCR-17-0582>.
DTP can be used as a design and an operational tool and can be displayed
as a table or flow diagram. The 'dtpcrm' package also provides the
modified continual reassessment method (CRM) and time-to-event CRM
(TITE-CRM) with added practical considerations to allow stopping early
when there is sufficient evidence that the lowest dose is too toxic and/or
there is a sufficient number of patients dosed at the maximum tolerated
dose.

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
