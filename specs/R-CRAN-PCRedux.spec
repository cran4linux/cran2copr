%global packname  PCRedux
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Quantitative Polymerase Chain Reaction (qPCR) Data Mining andMachine Learning Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bcp 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-chipPCR 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-MBmca 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-qpcR 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-bcp 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-chipPCR 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-MBmca 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-qpcR 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Extracts features from amplification curve data of quantitative Polymerase
Chain Reactions (qPCR) (Pabinger S. et al. (2014)
<doi:10.1016/j.bdq.2014.08.002>) for machine learning purposes. Helper
functions prepare the amplification curve data for processing as
functional data (e.g., Hausdorff distance) or enable the plotting of
amplification curve classes (negative, ambiguous, positive). The hookreg()
and hookregNL() functions (Burdukiewicz M. et al. (2018)
<doi:10.1016/j.bdq.2018.08.001>) can be used to predict amplification
curves with an hook effect-like curvature. The pcrfit_single() function
can be used to extract features from an amplification curve.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/decision_res_batsch1.csv
%doc %{rlibdir}/%{packname}/decision_res_batsch2.csv
%doc %{rlibdir}/%{packname}/decision_res_batsch3.csv
%doc %{rlibdir}/%{packname}/decision_res_batsch4.csv
%doc %{rlibdir}/%{packname}/decision_res_batsch5.csv
%doc %{rlibdir}/%{packname}/decision_res_boggy.csv
%doc %{rlibdir}/%{packname}/decision_res_C126EG595.csv
%doc %{rlibdir}/%{packname}/decision_res_C127EGHP.csv
%doc %{rlibdir}/%{packname}/decision_res_C316.amp.csv
%doc %{rlibdir}/%{packname}/decision_res_C317.amp.csv
%doc %{rlibdir}/%{packname}/decision_res_C60.amp.csv
%doc %{rlibdir}/%{packname}/decision_res_CD74.csv
%doc %{rlibdir}/%{packname}/decision_res_competimer.csv
%doc %{rlibdir}/%{packname}/decision_res_dil4reps94.csv
%doc %{rlibdir}/%{packname}/decision_res_guescini1.csv
%doc %{rlibdir}/%{packname}/decision_res_guescini2.csv
%doc %{rlibdir}/%{packname}/decision_res_HCU32_aggR.csv
%doc %{rlibdir}/%{packname}/decision_res_htPCR.csv
%doc %{rlibdir}/%{packname}/decision_res_karlen1.csv
%doc %{rlibdir}/%{packname}/decision_res_karlen2.csv
%doc %{rlibdir}/%{packname}/decision_res_karlen3.csv
%doc %{rlibdir}/%{packname}/decision_res_lc96_bACTXY.csv
%doc %{rlibdir}/%{packname}/decision_res_lievens1.csv
%doc %{rlibdir}/%{packname}/decision_res_lievens2.csv
%doc %{rlibdir}/%{packname}/decision_res_lievens3.csv
%doc %{rlibdir}/%{packname}/decision_res_RAS002.csv
%doc %{rlibdir}/%{packname}/decision_res_RAS003.csv
%doc %{rlibdir}/%{packname}/decision_res_reps.csv
%doc %{rlibdir}/%{packname}/decision_res_reps2.csv
%doc %{rlibdir}/%{packname}/decision_res_reps3.csv
%doc %{rlibdir}/%{packname}/decision_res_reps384.csv
%doc %{rlibdir}/%{packname}/decision_res_rutledge.csv
%doc %{rlibdir}/%{packname}/decision_res_stepone_std.csv
%doc %{rlibdir}/%{packname}/decision_res_testdat.csv
%doc %{rlibdir}/%{packname}/decision_res_vermeulen1.csv
%doc %{rlibdir}/%{packname}/decision_res_vermeulen2.csv
%doc %{rlibdir}/%{packname}/decision_res_VIMCFX96_60.csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/HCU32_aggR.csv
%doc %{rlibdir}/%{packname}/hookreg.rdml
%doc %{rlibdir}/%{packname}/PCRedux-app
%doc %{rlibdir}/%{packname}/RAS002.rdml
%doc %{rlibdir}/%{packname}/RAS003.rdml
%doc %{rlibdir}/%{packname}/Table_human_rated.xlsx
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
