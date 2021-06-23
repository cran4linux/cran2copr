%global __brp_check_rpaths %{nil}
%global packname  clinPK
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          Clinical Pharmacokinetics Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-curl 

%description
Calculates equations commonly used in clinical pharmacokinetics and
clinical pharmacology, such as equations for dose individualization,
compartmental pharmacokinetics, drug exposure, anthropomorphic
calculations, clinical chemistry, and conversion of common clinical
parameters. Where possible and relevant, it provides multiple published
and peer-reviewed equations within the respective R function.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bfa_boys_p_exp.txt
%doc %{rlibdir}/%{packname}/bfa_girls_p_exp.txt
%doc %{rlibdir}/%{packname}/bmi_boys_perc_WHO2007_exp.txt
%doc %{rlibdir}/%{packname}/bmi_girls_perc_WHO2007_exp.txt
%doc %{rlibdir}/%{packname}/hfa_boys_perc_WHO2007_exp.txt
%doc %{rlibdir}/%{packname}/hfa_girls_perc_WHO2007_exp.txt
%doc %{rlibdir}/%{packname}/lhfa_boys_p_exp.txt
%doc %{rlibdir}/%{packname}/lhfa_boys_z_exp.txt
%doc %{rlibdir}/%{packname}/lhfa_girls_p_exp.txt
%doc %{rlibdir}/%{packname}/lhfa_girls_z_exp.txt
%doc %{rlibdir}/%{packname}/wfa_boys_p_exp.txt
%doc %{rlibdir}/%{packname}/wfa_boys_perc_WHO2007_exp.txt
%doc %{rlibdir}/%{packname}/wfa_girls_p_exp.txt
%doc %{rlibdir}/%{packname}/wfa_girls_perc_WHO2007_exp.txt
%doc %{rlibdir}/%{packname}/wfh_boys_p_exp.txt
%doc %{rlibdir}/%{packname}/wfh_girls_p_exp.txt
%doc %{rlibdir}/%{packname}/wfl_boys_p_exp.txt
%doc %{rlibdir}/%{packname}/wfl_girls_p_exp.txt
%{rlibdir}/%{packname}/INDEX
