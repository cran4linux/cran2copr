%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  decompML
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decomposition Based Machine Learning Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-nnfor 
BuildRequires:    R-CRAN-Rlibeemd 
BuildRequires:    R-CRAN-VMDecomp 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-nnfor 
Requires:         R-CRAN-Rlibeemd 
Requires:         R-CRAN-VMDecomp 

%description
The hybrid model is a highly effective forecasting approach that
integrates decomposition techniques with machine learning to enhance time
series prediction accuracy. Each decomposition technique breaks down a
time series into multiple intrinsic mode functions (IMFs), which are then
individually modeled and forecasted using machine learning algorithms. The
final forecast is obtained by aggregating the predictions of all IMFs,
producing an ensemble output for the time series. The performance of the
developed models is evaluated using international monthly maize price
data, assessed through metrics such as root mean squared error (RMSE),
mean absolute percentage error (MAPE), and mean absolute error (MAE). For
method details see Choudhary, K. et al. (2023).
<https://ssca.org.in/media/14_SA44052022_R3_SA_21032023_Girish_Jha_FINAL_Finally.pdf>.

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
