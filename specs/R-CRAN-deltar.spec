%global packname  deltar
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of Delta R Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Bchron 
Requires:         R-CRAN-Bchron 

%description
Computes the regional correction factor of 14C age offset in
marine-derived samples (Delta R). This is possible with the recently
established "marine13" calibration curve and the 'BchronCalibrate'
function from the 'Bchron' package. The algorithm of Delta R computation
includes four steps: measure radiocarbon age of a marine sample; identify
its true age; compute its modeled radiocarbon age corresponding to the
true age; and finally calculate the difference between its measured and
modeled radiocarbon ages. This package has functions that compute Delta R
with three methods: by using marine samples with known collection dates
(before 1950s), usually molluscan shells from museum collections,
(function dr_shell()); by measuring other radioactive isotopes, mainly
uranium-thorium (230Th/234U), ratio (dr_pair() function and the "pair"
method in the dr_df() function); and finally by using a pair of coeval
samples, one being marine and the other terrestrial (dr_pair() function
and the "pair" method for the dr_df() function as well). Usually such
samples originate from archaeological sites where the context, in which
paired samples were found, is taken as a guarantee of their synchronicity.
References: Oeschger H, Siegenthaler U, Schotterer U, Gugelmann A (1975)
<doi:10.3402/tellusa.v27i2.9900> Reimer PJ, Bard E, Bayliss A, Beck JW,
Blackwell PG, Bronk Ramsey C, Buck CE, Cheng H, Edwards RL, Friedrich M,
Grootes PM, Guilderson TP, Haflidason H, Hajdas I, Hatté C, Heaton TJ,
Hoffmann DL, Hogg AG, Hughen KA, Kaiser KF, Kromer B, Manning SW, Niu M,
Reimer RW, Richards DA, Scott EM, Southon JR, Staff RA, Turney CSM, van
der Plicht J (2013) <doi:10.2458/azu_js_rc.55.16947> Soulet G (2015)
<doi:10.1016/j.quageo.2015.05.023> Stuiver M, Braziunas TF (1993)
<doi:10.1017/S0033822200013874> .

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
